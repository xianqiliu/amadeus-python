from amadeus import Client, ResponseError

amadeus = Client(
    client_id='REPLACE_BY_YOUR_OWN_ID',
    client_secret='REPLACE_BY_YOUR_OWN_SECRET'
)

try:
    response = amadeus.shopping.flight_offers_search.get(
        originLocationCode='MAD',
        destinationLocationCode='ATH',
        departureDate='2022-11-01',
        adults=1)
    print(response.data)
except ResponseError as error:
    print(error)
