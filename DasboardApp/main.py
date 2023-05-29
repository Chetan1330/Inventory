import time
from create_payouts import CreatePayouts
from get_payouts import GetPayouts
from get_payout_item import GetPayoutItem

print('Creating Payouts')
create_response = CreatePayouts().create_payouts(True)
if create_response.status_code == 201:
    batch_id = create_response.result.batch_header.payout_batch_id
    print('Retrieving Payouts batch with id: ' + batch_id)
    get_response = GetPayouts().get_payouts(batch_id, True)
    if get_response.status_code == 200:
        item_id = get_response.result.items[0].payout_item_id
        print('Retrieving Payout item with id: ' + item_id)
        get_item_response = GetPayoutItem().get_payout_item(item_id, True)
        if get_item_response.status_code == 200:
            print(
                'Check Payouts status to see if it has completed processing all payments')
            get_response = GetPayouts().get_payouts(batch_id, True)
            if get_response.result.batch_header.batch_status == "SUCCESS":
                print('Completed Payement Successfully')
                

    else:
        print('Failed to retrieve Payouts batch with id: ' + batch_id)
else:
    print('Failed to create Payouts batch')

# Execute all failure cases
#print('Create a payout with validation failure')
#CreatePayouts().create_payouts_failure(True)
#print('Retrieving an invalid payout')
#GetPayouts().get_payouts("DUMMY", True)
#print('Retrieving an invalid payout item')
#GetPayoutItem().get_payout_item("DUMMY", True)