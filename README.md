# silvr-client

A Python client for brokers to send new application.

```python
import silvr


with silvr.SilvrClient(auth=silvr.PasswordAuth(email, password)) as silvr_client:
    application = silvr_client.new_application(company_name, country, siret)
    application.bank_statements.add(file)
    application.financial_statements.add(file)
    application.save()
```
