class ShopperMemoryPreferenceProfileClient:
    def update_and_retrieve_shopper_memory(self, user_id='usr_elena_9918', new_observed_signals={'preferred_shoe_size': '8.5', 'favorite_color_palette': ['earth tones', 'forest green'], 'dietary_restrictions': ['gluten-free']}):
        return {
            'memory_profile_id': 'mem_prf_7721',
            'user_id': user_id,
            'persisted_shopper_profile': {
                'sizing_matrix': {'shoes': '8.5 US', 'tops': 'M', 'bottoms': '28W'},
                'aesthetic_preferences': ['earth tones', 'minimalist utilitarian', 'sustainable fabrics'],
                'brand_affinity_scores': {'Patagonia': 0.94, 'Arc-teryx': 0.88, 'Veja': 0.82},
                'lifetime_orders_count': 14
            },
            'personalized_affinity_vector_url': 'https://memory.shopper.genpark.ai/users/9918.json'
        }
