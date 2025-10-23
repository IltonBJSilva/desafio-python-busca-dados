from haversine import haversine, Unit

#Função para calcular distância geográfica:
def distance_km(lat1, lon1, lat2, lon2):
    if None in(lat1, lon1, lat2, lon2):
        return float("inf")
    return haversine((lat1, lon1), (lat2, lon2), unit=Unit.KILOMETERS)



"""
Explicativo sobre a função:

haversine: é uma função que calculo a distancia em linha reta entre dois pontos na superfice da Terra
usando a formula de Haversine. Ela considera a curvatura do planeta, então é mais precisa que so pegar a diferença
de latitude/Logintude.


"""