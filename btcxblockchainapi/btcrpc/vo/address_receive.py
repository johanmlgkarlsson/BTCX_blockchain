from rest_framework import serializers

class AddressReceiveInputParaMeter(object):
    
    def __init__(self, apikey="", currency="btc", amount=0, address="", test=False, confirms = 0):
       
        self._apikey = apikey
        self._currency = currency
        self._amount = amount
        self._address = address
        self._test = test
        self._confirms = confirms  
            
    @property
    def apikey(self):
        return self._apikey

    @apikey.setter
    def apikey(self, value):
        self._apikey = value

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
        
    @property
    def test(self):
        return self._test

    @test.setter
    def test(self, value):
        self._test = value

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value     

    @property
    def confirms(self):
        return self._confirms

    @confirms.setter
    def confirms(self, value):
        self._confirms = value
        
class AddressReceiveInputSerializer(serializers.Serializer):

    apikey = serializers.CharField(max_length=200)
    currency = serializers.CharField(max_length=20)
    test = serializers.BooleanField();
    address = serializers.CharField(max_length=200)
    amount = serializers.FloatField()
    confirms = serializers.IntegerField()

class AddressReceiveOutput(object):
    def __init__(self):
        self._state = "pending"
        self._currency = "btc"
        self._amount = 0.0
        self._address = ""
        self._message = None
        self._test = False
        self._amountreceived = 0.0
        
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
        

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    @property
    def test(self):
        return self._test

    @test.setter
    def test(self, value):
        self._test = value

    @property
    def amountreceived(self):
        return self._amountreceived

    @amountreceived.setter
    def amountreceived(self, value):
        self._amountreceived = value
    
        
class AddressReceiveOutputSerializer(serializers.Serializer):

    state = serializers.CharField(max_length=15)
    currency = serializers.CharField(max_length=20)
    amount = serializers.FloatField()
    address = serializers.CharField(max_length=200)
    message = serializers.CharField(max_length=200)
    test = serializers.BooleanField()
    amountreceived = serializers.FloatField()
