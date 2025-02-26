def outer_function():
    print("Hello from the outer function")
    
    def inner_function():
        print("Hello from the inner function")
        
    inner_function()
        
outer_function()