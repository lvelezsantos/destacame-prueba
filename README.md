# destacame prueba tecnica

## Enunciado

    El requerimiento es el siguiente:
    
    
    Una agencia de buses necesita una plataforma para gestionar sus viajes. 
    El sistema debe permitir que se ingresen diversos trayectos. Cada trayecto 
    tendrá varios buses asignados a distintos horarios. Cada bus tendrá un solo
    chofer y varios pasajeros asignados a sus asientos. Todos los buses tienen 
    la misma capacidad de 10 pasajeros sentados. Los asientos son numerados y 
    se reservan para cada pasajero. El sistema debe soportar el ingreso de pasajeros 
    a un trayecto y horario en particular, además de permitir la asignación de choferes 
    a sus respectivos buses.
    
    Modelo de datos
    Escriba a continuación las tablas que utilizaría para resolver este problema 
    con los campos y llaves de éstas. Intente hacer el sistema lo más robusto 
    posible, pero sin incluir datos adicionales a los que se plantean acá.
    
    Backend
    Si usted estuviera resolviendo el problema de la agencia de buses implementando 
    una aplicación web que incluya las siguientes funcionalidades:
    
    CRUD pasajeros, choferes, trayectos, buses.
    Listar a los trayectos junto a su promedio de pasajeros.
    Filtrar a todos los buses de un trayecto con más del N % de su capacidad vendida.
    Para la implementación hay que utilizar el Django y su ORM.
    
    Nota:
        - La aplicación debe incluir un archivo README.md explicando como 
    instalar las dependencias del proyecto. así como todos los supuestos 
    considerados, se recomienda el uso de APIs en el desarrollo del test. 
    (si las instrucciones no logran que el proyecto corra, el mismo no sera evaluado)
        
        - Utilizar Vue.js, Django APIRest Framework.



### Modelo de Datos

    - Place (Lugar)
        * id: pk
        * name: unique
        * description
        
    - Route (Ruta - Trayecto)
        * id: pk
        * source: fk Place
        * destination: fk Place
        
    - Driver (Conductor)
        * id: pk
        * name: unique
        
    - Bus (Bus)
        * id: pk
        * driver: fk Driver
        * capacity
        
    - Passenger (Pasajero)
        * id: pk
        * name
        * identification
    
    - Schedule (Programacion de Ruta)
        * id: pk
        * start
        * end
        * bus: fk Bus
        * route: fk Route
    
    - PassengerSchedule (Asiento Pasajero)
        * id: pk
        * schedule: fk Schedule
        * passenger: fk Passenger
        * seat


### Pasos para ejecucion

1. Instalar Docker  https://docs.docker.com/get-docker/
2. Instalar Docker Compose  https://docs.docker.com/compose/install/
3. Hacer ejecutable el archivo install.sh 
    
    
    chmod +x install.sh
    
4. ejecutar el archivo install.sh:
    

    sh ./install.sh
    or
    ./install.sh
    
    
5. Front: http://localhost:9030/
6. Api: http://localhost:9020/api/


Nota:
    
    * debe asegurar que los puertos 9030 y 9020 estan disponibles. 
    * Sino esta configurado docker para usar sin superusuario, execute el archivo de 
    install.sh con sudo o con el user root
   
  