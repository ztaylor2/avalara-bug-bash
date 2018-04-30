"""Attempting to find bugs in Avalara API."""

from client import AvataxClient


def create_client():
    """
    Construct a new AvaTaxClient in a Sandbox Environment
    'test app': The name of the application
    'ver 0.0': Version number of the application
    'test machine': Name of the machine on which this code is executing
    Add credentials to configure client to use the specified username/password security settings.
    Your Sandbox username and password should be set as environment variables prior to executing the request.
    Return example_client.
    """
    example_client = AvataxClient('codefellowsTestApp', 'ver 0.0', 'test machine')
    example_client.add_credentials('ted+codefellows@spence.net', '4C87ABA1091')
    return example_client


def example_create_transaction():
    """
    Assign example_client to the SandboxClient instance returned from create_client().
    The tax document dictionary is used as a transaction model in the
    create transaction request.
    'addresses': Addresses for all lines in the document
    'commit': Set to false so the document will not be committed
    'companyCode': Specifies the account's default company creating the transaction
    'currenyCode': The three-character ISO 4217 currency code for the transaction
    'customerCode': The client application customer reference code
    'date': The date on the invoice
    'description': Description for the transaction
    'lines': List of line items that will appear on the transaction
    'purchaseOrderNo': Purchase Order Number for the document
    'type': Specifies permanent transaction document that will be recorded
    Return example_client with the create_transaction method, passing in the arugments None and tax_document.
    """
    example_client = create_client()
    tax_document = {
        'addresses':
            {'SingleLocation':
                {'city': 'Mercer Island',
                 'country': 'US',
                 'line1': '8007 SE 60th St',
                 'postalCode': '98040',
                 'region': 'WA'
                 }},
        'commit': False,
        'companyCode': None,
        'currencyCode': 'USD',
        'customerCode': 'ABC',
        'date': '2017-04-12',
        'description': 'Yarn',
        'lines': [{'amount': 100,
                   'description': 'Yarn',
                   'itemCode': 'Y0001',
                   'number': '1',
                   'quantity': 1,
                   'taxCode': 'PS081282'}],
        'purchaseOrderNo': '2017-04-12-001',
        'type': 'SalesInvoice'}

    return example_client.create_transaction(tax_document)


if __name__ == '__main__':
    response = example_create_transaction()
    print(response.json()['totalTaxCalculated'])
    # import pdb; pdb.set_trace()
