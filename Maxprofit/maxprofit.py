list1 = [0] * 3
time_required = [5, 4, 10]
cost_per_item = [1500, 1000, 3000]
input_time = int(input("Enter the time: "))
results = []
configurations = []

def find_max_profit_recursive(index, current_time, current_profit, current_configuration):
    if index == len(time_required):
        if current_time != 0:
            for i in range(len(cost_per_item)):
                if current_configuration[i] != 0:
                    current_profit += current_time * cost_per_item[i] * current_configuration[i]
        
        results.append(current_profit)
        configurations.append(current_configuration.copy())
        return
    
    if current_time - time_required[index] >= 0:
        if current_configuration:
            for i in range(len(cost_per_item)):
                if current_configuration[i] != 0:
                    current_profit += time_required[index] * cost_per_item[i] * current_configuration[i]
        
        current_configuration[index] += 1
        find_max_profit_recursive(index, current_time - time_required[index], current_profit, current_configuration)
        current_configuration[index] -= 1
        if current_configuration:
            for i in range(len(cost_per_item)):
                if current_configuration[i] != 0:
                    current_profit -= time_required[index] * cost_per_item[i] * current_configuration[i]
    find_max_profit_recursive(index + 1, current_time, current_profit, current_configuration)

find_max_profit_recursive(0, input_time, 0, list1)

max_profit = max(results)
max_profit_configs = []
for idx, result in enumerate(results):
    if result == max_profit:
        max_profit_configs.append(idx)

original_configs = []
for idx in max_profit_configs:
    original_configs.append(configurations[idx])

formatted_configs = [{'Time': config[0], 'Profit': config[1], 'Cost': config[2]} for config in original_configs]

print(f'Maximum Profit: {max_profit}')
for config in formatted_configs:
    print(config)

