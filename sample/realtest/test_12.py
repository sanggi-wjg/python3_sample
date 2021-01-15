sample = {
    'Response': {
        'Code'   : '0000',
        'Success': 'success',
    }
}

response = sample['Response']
print(response)

if 'Detail' in response:
    print('Yes')
else:
    print('No')
