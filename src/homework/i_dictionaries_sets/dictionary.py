#Main functions

def add_inventory(widgets, widget_name, quantity):
    # Check if the widget_name exists in the dictionary
    if widget_name in widgets:
        # If it exists, update the quantity
        widgets[widget_name] += quantity
    else:
        # If it doesn't exist, add a new entry
        widgets[widget_name] = quantity

def remove_inventory_widget(widgets, widget_name):
    # Check if the widget_name exists in the dictionary
    if widget_name in widgets:
        # If it exists, remove it and return 'Record deleted'
        del widgets[widget_name]
        return 'Record deleted'
    else:
        # If it doesn't exist, return 'Item not found'
        return 'Item not found'