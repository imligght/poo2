times_dict = {}
count_names = 0

for i in range(6):
    count_names += 1
    name = input(f'\nDigite o nome do {count_names}° piloto/corredor: \n')
    try:
        times = list(map(int, input('Digite seus 10 tempos, em segundos, separados por espaços: \n').split()))
    except ValueError:
        print('Certifique-se de inserir apenas valores inteiros para os tempos.')
        continue

    times_dict[name] = times

print('\nTempos dos pilotos:')
for name, time in times_dict.items():
    print(f'{name}: {time}')

def best_lap():
    best_laps = {}
    for name in times_dict.keys():
        best_lap_time = min(times_dict[name])
        best_lap_index = times_dict[name].index(best_lap_time) + 1
        best_laps[name] = (best_lap_time, best_lap_index)

    first_pilot, (first_time, first_time_index) = list(best_laps.items())[0]
    pilot_with_best_time = first_pilot
    best_time, best_time_index = (first_time, first_time_index)

    for name, (time, time_index) in best_laps.items():
        if time < best_time:
            best_time = time
            pilot_with_best_time = name
            best_time_index = time_index

    return {pilot_with_best_time: (best_time, best_time_index)}

def construct_podium():
    average_time_dict = {}
    for pilot, times in times_dict.items():
        average_time_dict[pilot] = sum(times) / len(times)

    average_time_dict = dict(sorted(average_time_dict.items(), key=lambda item: item[1]))

    return average_time_dict

print(f'\nPiloto com o melhor tempo: ')
for name, (time, time_index) in best_lap().items():
    print(f'{name} teve o melhor tempo performado, terminando uma volta completa em {time} segundos na rodada {time_index}!\n')

for i, (pilot, average_time) in enumerate(construct_podium().items(), start=1):
    print(f'{pilot} ficou em {i}° lugar com uma média de tempo de {average_time:.2f} segundos por volta!' )
