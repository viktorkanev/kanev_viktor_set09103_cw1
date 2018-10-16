def Artists():
    artists = [
        {
            'id': 1,
            'name': 'Eminem',
            'genre': 'Hip Hop',
            'albums': [{
                'title': 'Relapse',
                'release_date': '15-05-2009',
                'songs': '20'
            },
                {
                    'title': 'Recovery',
                    'release_date': '18-10-2010',
                    'songs': '17'
            }]
        },
        {
            'id': 2,
            'name': '50 cent',
            'genre': 'Hip Hop',
            'albums': [{
                'title': 'Get Rich or Die Tryin\'',
                'release_date': '6-02-2013',
                'songs': '16'
            },
                {
                    'title': 'The Massacre',
                    'release_date': '3-03-2005',
                    'songs': '22'
                }]
        },
        {
            'id': 3,
            'name': 'Eagles',
            'genre': 'Rock',
            'albums': [{
                'title': 'Hotel California',
                'release_date': '08-12-1976',
                'songs': '19'
            },
                {
                    'title': 'Desperado',
                    'release_date': '17-04-1973',
                    'songs': '11'
                }]
        },
        {
            'id': 4,
            'name': 'Kings Of Leon',
            'genre': 'Rock',
            'albums': [{
                'title': 'Only by the Night',
                'release_date': '19-09-2008',
                'songs': '13'
            },
                {
                    'title': 'Walls',
                    'release_date': '14-10-2016',
                    'songs': '10'
                }]
        }
    ]
    return artists