INTRODUCCION = '''INICIO DE LA EXPEDICIÓN
El helicóptero se estrella en Svalbard. El frío es antinatural. 
Una explosión minera ha liberado un hongo milenario que zombifica todo a su paso. 
A lo lejos, el Gran Yeti ruge con furia. 
Deben adentrarse en la montaña, detener la infección y sobrevivir...'''

TRANSICION_1 = '''PISTA VERDE SUPERADA
Dejan atrás los senderos nevados. Llegan a las instalaciones mineras. 
Los trabajadores que causaron este desastre siguen aquí, controlados por el hongo...'''

TRANSICION_2 = '''PISTA AMARILLA SUPERADA
El hielo negro cruje. Han superado el campamento, pero la infección es total. 
Se acercan al epicentro. Algo inmenso los vigila entre la ventisca...'''

REFUGIO_MILITAR = '''ZONA SEGURA
Encuentran un refugio intacto con un Desfibrilador de Adrenalina. 
El equipo recupera el aliento y limpia sus heridas de la necrosis. 
(Salud restaurada al 100% y Segunda Oportunidad obtenida)'''

APARICION_YETI = '''PELIGRO CRÍTICO - APARICIÓN DEL JEFE SUPREMO 
El Gran Yeti bloquea la cumbre. Sus ojos brillan con furia ciega. 
Busca erradicar la plaga humana a toda costa. PREPARARSE PARA COMBATIR '''

AVALANCHA = '''SE APROXIMA UNA AVALANCHA
El Yeti herido golpea el glaciar. Bloques de hielo gigantes comienzan a caer sobre el equipo'''

ADRENALINA_USADA = ''' SE ACTIVÓ SU SEGUNDA OPORTUNIDAD
El equipo cae, pero el Desfibrilador automático se dispara. 
Un choque eléctrico los reanima para un último intento en la gran batalla '''

VICTORIA = ''' VICTORIA 
El gigante cae exhausto y retrocede. Ha comprendido que no son el enemigo. 
El hongo comienza a ceder. Lograron sobrevivir al Misterio Alpino '''

ACERTIJO_1 = '''El sendero se divide y una tormenta se acerca. ¿Por dónde siguen?
1. Por el puente de hielo, que tiene grietas pero es el camino más corto
2. Por el borde del bosque, siguiendo las marcas de los mineros
3. Por el fondo del valle, donde se acumula la nieve de las laderas'''

ACERTIJO_2 = '''Una nota en la pared dice: "El hongo duerme en lo oscuro y huye del fuego".
Tres puertas llevan a la salida del campamento. ¿Cuál eligen?
1. La del túnel sin luz
2. La del depósito inundado
3. La de la sala de calderas, todavía encendidas'''

ACERTIJOS = {"pista_verde": (ACERTIJO_1, 2), "pista_amarilla": (ACERTIJO_2, 3)}

DERROTA = '''GAME OVER
El frío y la infección terminan el trabajo. 
La patrulla ahora es parte del eterno hielo de Svalbard'''