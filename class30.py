RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade = 61
local_carro = 99

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (
    LOCAL_1 + RADAR_RANGE
)
carro_multado_radar_1 = velocidade_carro_passou_radar_1 and carro_passou_radar_1


if velocidade_carro_passou_radar_1:
    print("Velocidade carro passou do radar 1")

if carro_multado_radar_1:
    print("Carro multado em radar 1")
