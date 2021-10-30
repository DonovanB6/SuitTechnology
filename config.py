
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
                'patterns': ['Internship', 'Tell me about internships', 'Are there any internships available?','What '
                'internship opprtunities are available?' ],
                'responses': ['Yes, here\'s a link to an internship: www.blah.com', 'Here\'s  a link to availiable in'
                'ternships that might interest you: www.blah.com', 'Here is a link to an internship I think you might' 
                'be interested in: www.blah.com']
            },
            {
                'message_type': 'Scholarships',
                'patterns': ['Scholarships','Tell me about scholarships', 'What scholarships are available?', 'Are th'
                'ere any scholarship opportunities avalable?',],
                'responses': ['Sure, I think this Scholarship might interest you: www.blah.com', 'Yes, here\'s a link'
                ' to a scholarship: www.blah.com','Here\'s a link to a scholarship you might be interested in: www.bl'
                'ah.com']
            },
            {
                'message_type':'Work Studies',
                'patterns': ['Work Studies', 'Tell me about work studies', 'What work studies are available?','Are th'
                'ere any work studies available?'],
                'responses': ['Sure, here is a link to a work study: www.blah.com','Here is a link to a work study: w'
                'ww.blah.com','Here\'s a link to a work study that you might be interested in: www.blah.com']
            },
            {
                'message_type': 'Thanking',
                'patterns': ['Thanks for your help', 'Thank you','Thanks','Gracias',],
                'responses': ['No Problem!','I\'m happy to help!','My Pleasure!', 'I\'m glad I was able to help!' 'No'
                ' Problem, is there anything else I can help you with?','No Problem, is there another opportunity you'
                ' would like to learn about?']
            },
            {
                'message_type': 'Closing',
                'patterns': ['Goodbye','Bye','Adios','No, Thanks for your help!'],
                'responses': ['Okay, have a good rest of your day!', 'Okay, Goodbye!','I\'m glad I was able to assist' 
                ' you, goodbye!','Bye!']
            },
            {
                'message_type': 'Inspirational',
                'patterns': ['I\'m feeling uninspired', 'Inspire me','I need some insipration','I need some Inspirati'
                'on','Give me an Inspirational quote'],
                'responses': ['The best view comes after the hardest climb.','Believe you can and you\'re halfway the'
                're.','Nothing is impossible, the word itself says "I\'m Possible!']
            },
            {
                'message_type': 'Motivational',
                'patterns': ['I\'m feeling unmotivated', 'Motivate me','What is a motivational quote?','I need some m'
                'otivation','Give me a motivational quote'],
                'responses': ['Victory requires payment in advance','The only time you fail is when you fall and stay'
                ' down.','There are no shortcuts to any place worth going.','Strive for progress, not perfection.']
            },
            {
                'message_type': 'Sad',
                'patterns': ['I\'m feeling sad','I\'m sad', 'I\'m feeling down','Give me an uplifting quote'],
                'responses': ['No one is perfect, that\'s why pencils have erasers.','Live life to its fullest and fo'
                'cus on the positive','You always pass failure on the way to success']
            }
        ]
    }
]