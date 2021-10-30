
flow = [
    {
        'id': 'flow1',
        'is_linear_conversation': True,
        'message_options': [{
                'message_type': 'greeting',
                'patterns': ['Hello', 'Hey', 'Hi', 'Hey there', 'What\'s up?', 'Hola', 'Top of the morning'],
                'responses': ['Hello there, how can I help?', 'Hello friend, what can I do for you', 'Hey, how can I '
                                                                                                     'help you?'],
            },
            {
                'message_type': 'internships',
                'patterns': ['Internship', 'Tell me about internships', 'Are there any internships available?', ],
                'responses': ['Yes, here\'s a link to an internship: www.blah.com', '' ]
            },
        ]
    }
]