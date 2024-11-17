def decideorderquantitycontroller(current_price, stock_level, average_price, critical_stock_level=10, min_order_quantity=10, discount_threshold=0.2):

    threshold_price = average_price * (1 - discount_threshold)
    
    is_discounted = current_price <= threshold_price
    
    is_stock_critical = stock_level < critical_stock_level
    
    if is_discounted:
        if is_stock_critical:
            return min_order_quantity  
        else:
            return 15  
    elif is_stock_critical:
        return min_order_quantity  
    
    return 0  
