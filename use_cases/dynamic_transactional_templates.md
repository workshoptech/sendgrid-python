# Transactional Templates

For this example, we assume you have created a [dynamic transactional template](https://sendgrid.com/docs/User_Guide/Transactional_Templates/how_to_send_an_email_with_transactional_templates.html). Following is the template content we used for testing.

Template ID (replace with your own):

```text
d-5b08559ac97289da39defbb521bc62da
```

Email Subject:

```text
{{subject}}
```

Template Body:

```html
<html>
<head>
    <title></title>
</head>
<body>
Hello {{name}},
<br /><br/>
I'm glad you are trying out the template feature!
{{#if city}}
<br /><br/>
I hope you are having a great day in {{city.name}}, {{city.country}} :)
{{/if}}
<br /><br/>
</body>
</html>
```

## With Mail Helper Class

```python
import sendgrid
import os
from sendgrid.helpers.mail import Email, DynamicData, Mail, Personalization
try:
    # Python 3
    import urllib.request as urllib
except ImportError:
    # Python 2
    import urllib2 as urllib

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("test@example.com")
to_email = Email("test@example.com")
mail = Mail(from_email, to_email)
personalization = Personalization()
personalization.add_dynamic_template_data(DynamicData("subject", "Dynamic Templating"))
personalization.add_dynamic_template_data(DynamicData("name", "Example User"))
personalization.add_dynamic_template_data(DynamicData("city", { "name": "Denver", "country": "USA" }))
mail.template_id = "d-5b08559ac97289da39defbb521bc62da"

try:
    response = sg.client.mail.send.post(request_body=mail.get())
except urllib.HTTPError as e:
    print (e.read())
    exit()
print(response.status_code)
print(response.body)
print(response.headers)
```

## Without Mail Helper Class

```python
import sendgrid
import os
try:
    # Python 3
    import urllib.request as urllib
except ImportError:
    # Python 2
    import urllib2 as urllib

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
data = {
  "personalizations": [
    {
      "to": [
        {
          "email": "test@example.com"
        }
      ],
      "dynamic_template_data": {
        "subject": "Dynamic Templating",
        "name": "Example User",
        "city": {
            "name": "Denver",
            "country": "USA"
        }
      },
    },
  ],
  "from": {
    "email": "test@example.com"
  },
  "template_id": "d-5b08559ac97289da39defbb521bc62da"
}
try:
    response = sg.client.mail.send.post(request_body=data)
except urllib.HTTPError as e:
    print (e.read())
    exit()
print(response.status_code)
print(response.body)
print(response.headers)
```