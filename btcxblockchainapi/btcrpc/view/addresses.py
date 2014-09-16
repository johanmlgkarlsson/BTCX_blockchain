from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from btcrpc.utils import constantutil
from btcrpc.utils.btc_rpc_call import BTCRPCCall
from btcrpc.utils.log import get_log
from btcrpc.views import attributeConst
from btcrpc.vo import addresses

__author__ = 'sikamedia'
__Date__ = '2014-09-11'

log = get_log("create new addresses")


class CreateNewAddresses(APIView):

    def post(self, request):

        serializer_input = addresses.NewAddressesPostParametersSerializer(data=request.DATA)

        if serializer_input.is_valid():
            currency = serializer_input.data["currency"]
            wallet = serializer_input.data["wallet"]
            btc_rpc_call = BTCRPCCall(wallet=wallet,currency=currency)
            #check is testnet or not
            is_test_net = constantutil.check_service_is_test_net(btc_rpc_call)

            log.info(serializer_input.data["quantity"])
            new_addresses = []
            for x in xrange(0, int(serializer_input.data[attributeConst.QUANTITY])):
                new_address = btc_rpc_call.do_get_new_address()
                btc_rpc_call.do_set_account(new_address, new_address)
                new_addresses.append(new_address)

            new_addresses_response = addresses.NewAddresses(addresses=new_addresses, test=is_test_net)

            addresses_serializer = addresses.NewAddressesSerializer(data=new_addresses_response.__dict__)
            if addresses_serializer.is_valid():
                return Response(addresses_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(addresses_serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(serializer_input.errors, status=status.HTTP_400_BAD_REQUEST)