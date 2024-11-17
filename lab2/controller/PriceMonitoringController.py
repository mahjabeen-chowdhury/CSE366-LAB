def pricemonitoringcontroller(current_price, average_price, discount_threshold=0.2):

    threshold_price = average_price * (1 - discount_threshold)
    
    if current_price <= threshold_price:
        return True  
    return False  
