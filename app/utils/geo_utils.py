from haversine import haversine, Unit

#Função para calcular distância geográfica:
def distance_km(lat1, lon1, lat2, lon2):
    """
    Calcula a distância geográfica em quilômetros entre dois pontos na superfície da Terra.

    Utiliza a fórmula de Haversine, que considera a curvatura do planeta,
    fornecendo uma distância mais precisa que apenas a diferença de latitude/longitude.

    Parâmetros:
        lat1 (float): Latitude do ponto 1.
        lon1 (float): Longitude do ponto 1.
        lat2 (float): Latitude do ponto 2.
        lon2 (float): Longitude do ponto 2.

    Retorna:
        float: Distância em quilômetros entre os dois pontos. Retorna `inf` se algum dos valores for None.
    """
    if None in(lat1, lon1, lat2, lon2):
        return float("inf")
    return haversine((lat1, lon1), (lat2, lon2), unit=Unit.KILOMETERS)