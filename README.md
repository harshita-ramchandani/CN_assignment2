# CN_assignment2

## Part1
The file for Part1 has to be run using the command.

$sudo python3 mininet_Part1_a.py

You first have to ensure that you have the openvswitch installed in your system which can be done on kali linux using the commands.

$sudo apt-get install openvswitch-switch
$sudo service openvswitch-switch start

The system is made with 3 routers wich are connected to three switches, and those three switches are conneted to 2 hosts ech. This system is divided into 3 subnets as specified in the question and appropriate routings have been added to have a succesful connection.

The TCP dump is captured in wireshark given below

![alt text](https://github.com/harshita-ramchandani/CN_assignment2/blob/main/Screenshot%202023-11-11%20at%2022.52.37.png?raw=true)

The default route was varied, the route and the latency difference beacuse of ping and iperf both are added to the pdf shared in classroom and also available in this repository by the name [CN_Assgnment-2](https://github.com/harshita-ramchandani/CN_assignment2/blob/main/assignment2/CN_Assignment-2.pdf).

The routing table screenshot is also added above.

## Part2
The file in Part2 has to be run using the command

$sudo python3 mininet_Part2_a.py

The connection consist of 4 hosts and 2 switches divided into two subnets.

The throughput analysis were done using iperf3. All the screenshots can be found in the attached pdf.

The graph achieved was:

![alt text](https://raw.githubusercontent.com/harshita-ramchandani/CN_assignment2/main/WhatsApp%20Image%202023-11-12%20at%2006.03.43.jpeg)

The x-axis shows the time interval from time t=0sec to t=10sec, the y-axis shows the throughput.

Screenshots are also added for the throughput analysis with the link loss parameter of the middle link (s1 - s2) to 1% and 3%. The screenshots of the same are added in pdf attached.





