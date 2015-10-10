#search_by_words
This script makes a search in a text by words and return the sentences that were found.

## How does it work?
Follow an example:

```python
  from search_by_words import search_by_words

  text = """
  The term originally referred to messages sent using the Short Message Service (SMS).

  It may simply be referred to as a text in North America, the United Kingdom, Australia,
  New Zealand and the Philippines, an SMS in most of mainland Europe, and an MMS or SMS in
  the Middle East, Africa, and Asia.

  Text messages can be used to interact with automated systems to, for example, to order 
  products or services, or to participate in contests. Advertisers and service providers 
  use direct text marketing to message mobile phone.
  """

  search_by_words(text, 'SMS', 'MMS')
  """ ['The term originally referred to messages sent using the Short Message Service (SMS)', 
     'It may simply be referred to as a text in North America, the United Kingdom, Australia,
      New Zealand and the Philippines, an SMS in most of mainland Europe, and an MMS or SMS in
      the Middle East, Africa, and Asia.'] """
```

## Contributing
### Running tests
```shell
  python test.py
```
