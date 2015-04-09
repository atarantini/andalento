=========
andalento
=========

With *andalento* you can check your internet connection latency with various internet serrver providers that have ookla speedtest servers.

Run
---

Just call *andalento.py* from the terminal and will run all latency tests with the servers inside *servers-AR.json*:

.. code-block:: bash
    $ python andalento.py
    1) Buenos Aires/Fibertel (speed.fibertel.com.ar:8080): 26ms
    2) Buenos Aires/Silica Networks Argentina S.A. (cliente3.silicanetworks.net.ar:8080): 33ms
    3) Buenos Aires/Host-Engine.com (test.ar.host-engine.com:8080): 33ms
    4) Bahia Blanca/Silica Networks Argentina S.A. (cliente1.silicanetworks.net.ar:8080): 35ms
    5) Buenos Aires/Telecom Argentina (st1.telecom.com.ar:8080): 35ms
    6) Buenos Aires/Tele Red (www.telered.com.ar:8080): 36ms
    7) Ramos Mejia/Solunet.com.ar (speedtest.solunet.com.ar:8080): 37ms
    8) Buenos Aires/Telecentro (velocidad.telecentro.net.ar:8080): 37ms
    9) Rosario/FireHosted.com (test.firehosted.com:8080): 38ms
    10) Buenos Aires/Claro (speedtest.claro.com.ar:8080): 39ms
    11) Berisso/Horus Sistemas Informaticos SRL (st.horusnet.com.ar:8080): 44ms
    12) Pilar/Telconet S.A. (www.equal.com.ar:8080): 44ms
    13) Rosario/Telecom Argentina (stros1.telecom.com.ar:8080): 54ms
    14) Cordoba/Telecom Argentina (stcor1.telecom.com.ar:8080): 57ms
    15) Neuquen/Davitel S.A. (speedtest.nqntv.com.ar:8080): 76ms
    16) Canuelas/Internet Local (190.110.180.15:8080): 383ms
    17) El Calafate/COTECAL LTDA. (ooklaserver.cotecal.com.ar:8080): 437ms
    18) Curuzu Cuatia/VHG Sistemas (st1.curuzu.net:8080): 473ms


Servers
-------

As you can see, the server list used is from Argentina. A full list is provided in the *servers.xml*
file that was downloaded from http://c.speedtest.net/speedtest-servers-static.php, so feel free to
update the list as you see fit.

TO DO
-----

* Output results to json
* Interface to select the desired server
* Add Download/Upload tests


Author
------

Andres Tarantini (atarantini@gmail.com)