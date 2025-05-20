from enum import Enum
from typing import Dict, Optional, Any, List, Tuple

class SegmentType(Enum):
    """Tipos de segmentos de memoria"""
    GLOBAL = 'global'
    LOCAL = 'local'
    TEMP = 'temp'
    CONSTANT = 'constant'

class DataType(Enum):
    """Tipos de datos disponibles"""
    INT = 0
    FLOAT = 1
    BOOL = 2
    STRING = 3
    ERROR = -1

class MemoryManager:
    """
    Administrador de memoria virtual para BabyDuck
    
    Se encarga de asignar direcciones virtuales para variables, constantes y temporales
    """
    # Definición de rangos por segmento y tipo
    MEMORY_RANGES = {
        SegmentType.GLOBAL: {
            DataType.INT: (1000, 1999),
            DataType.FLOAT: (2000, 2999)
        },
        SegmentType.LOCAL: {
            DataType.INT: (3000, 3999),
            DataType.FLOAT: (4000, 4999)
        },
        SegmentType.TEMP: {
            DataType.INT: (5000, 5999),
            DataType.FLOAT: (6000, 6999),
            DataType.BOOL: (7000, 7999)
        },
        SegmentType.CONSTANT: {
            DataType.INT: (8000, 8999),
            DataType.FLOAT: (9000, 9999),
            DataType.STRING: (10000, 10999)
        }
    }

    def __init__(self):
        """Inicializa el administrador de memoria"""
        # Contadores para llevar el registro de las direcciones asignadas por segmento y tipo
        self.counters = {
            segment: {
                data_type: ranges[0]  # Inicializar con el rango inicial
                for data_type, ranges in segment_ranges.items()
            }
            for segment, segment_ranges in self.MEMORY_RANGES.items()
        }
        
        # Diccionario para mapear constantes a sus direcciones
        # Evita duplicados al asignar memorias múltiples veces para la misma constante
        self.constant_map = {}
        
        # Contador de temporales usados (para estadísticas)
        self.temp_counter = 0

    def get_address(self, segment: SegmentType, data_type: DataType) -> int:
        """
        Solicita una nueva dirección de memoria para el segmento y tipo indicados
        
        Args:
            segment: Segmento de memoria (GLOBAL, LOCAL, TEMP, CONSTANT)
            data_type: Tipo de dato (INT, FLOAT, BOOL, STRING)
            
        Returns:
            int: Dirección de memoria asignada
            
        Raises:
            MemoryError: Si se agota el espacio en el segmento solicitado
        """
        if segment not in self.MEMORY_RANGES or data_type not in self.MEMORY_RANGES[segment]:
            raise ValueError(f"Combinación inválida de segmento {segment} y tipo {data_type}")
        
        # Obtener el contador actual y el rango máximo
        current_count = self.counters[segment][data_type]
        _, max_range = self.MEMORY_RANGES[segment][data_type]
        
        # Verificar si hay espacio disponible
        if current_count > max_range:
            raise MemoryError(f"Se agotó el espacio en el segmento {segment.name} para tipo {data_type.name}")
        
        # Asignar la dirección y actualizar el contador
        address = current_count
        self.counters[segment][data_type] += 1
        
        # Incrementar el contador de temporales si aplica
        if segment == SegmentType.TEMP:
            self.temp_counter += 1
            
        return address

    def get_constant_address(self, value: Any) -> int:
        """
        Asigna o recupera una dirección para una constante
        
        Args:
            value: Valor de la constante
            
        Returns:
            int: Dirección de memoria asignada a la constante
        """
        # Si la constante ya tiene una dirección asignada, retornarla
        if value in self.constant_map:
            return self.constant_map[value]
        
        # Determinar el tipo de dato de la constante
        if isinstance(value, int):
            data_type = DataType.INT
        elif isinstance(value, float):
            data_type = DataType.FLOAT
        elif isinstance(value, str):
            # Verificar si es una cadena literal (con comillas)
            if value.startswith('"') and value.endswith('"'):
                data_type = DataType.STRING
            else:
                # Es un identificador, no una constante
                raise ValueError(f"'{value}' no es una constante válida")
        else:
            raise TypeError(f"Tipo de constante no soportado: {type(value)}")
        
        # Asignar una dirección para la constante
        address = self.get_address(SegmentType.CONSTANT, data_type)
        
        # Registrar la constante para evitar duplicados
        self.constant_map[value] = address
        
        return address

    def reset_local_counters(self):
        """Reinicia los contadores para el segmento local (al cambiar de función)"""
        for data_type in self.counters[SegmentType.LOCAL]:
            self.counters[SegmentType.LOCAL][data_type] = self.MEMORY_RANGES[SegmentType.LOCAL][data_type][0]
        
        # También reiniciamos los temporales, ya que se liberan al salir de una función
        for data_type in self.counters[SegmentType.TEMP]:
            self.counters[SegmentType.TEMP][data_type] = self.MEMORY_RANGES[SegmentType.TEMP][data_type][0]
        
        # Reiniciar contador de temporales
        self.temp_counter = 0

    def get_address_segment_type(self, address: int) -> Tuple[Optional[SegmentType], Optional[DataType]]:
        """
        Determina el segmento y tipo de dato correspondiente a una dirección
        
        Args:
            address: Dirección de memoria
            
        Returns:
            Tuple[Optional[SegmentType], Optional[DataType]]: Segmento y tipo de dato,
            o None, None si la dirección no es válida
        """
        for segment, segment_ranges in self.MEMORY_RANGES.items():
            for data_type, (start, end) in segment_ranges.items():
                if start <= address <= end:
                    return segment, data_type
        
        return None, None