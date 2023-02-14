
# Function that controls all other .py files except the ones responsible for interface
def start_process():

    import check_errors
    from check_errors import count_err
    
    if count_err == 0:

        import check_data_for_birthdays
        from check_data_for_birthdays import count_bir
        
        if count_bir > 0:

            import send_letters

start_process()