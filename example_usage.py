from client import ShopperMemoryPreferenceProfileClient

def main():
    client = ShopperMemoryPreferenceProfileClient()
    res = client.update_and_retrieve_shopper_memory('usr_alex_01')
    print('Shopper Memory Profile: ' + res['memory_profile_id'] + ' (User: ' + res['user_id'] + ')')
    print('Sizing: ' + str(res['persisted_shopper_profile']['sizing_matrix']))
    print('Affinities: ' + ', '.join(res['persisted_shopper_profile']['aesthetic_preferences']))
    print('Profile URL: ' + res['personalized_affinity_vector_url'])

if __name__ == '__main__':
    main()
