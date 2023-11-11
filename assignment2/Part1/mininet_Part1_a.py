from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.node import OVSController
from mininet.log import setLogLevel, info
from mininet.cli import CLI



class LinuxRouter( Node ):
    "A Node with IP forwarding enabled."

    # pylint: disable=arguments-differ
    def config( self, **params ):
        super( LinuxRouter, self).config( **params )
        # Enable forwarding on the router
        self.cmd( 'sysctl net.ipv4.ip_forward=1' )

    def terminate( self ):
        self.cmd( 'sysctl net.ipv4.ip_forward=0' )
        super( LinuxRouter, self ).terminate()



class NetworkTopo( Topo ):
    "A LinuxRouter connecting three IP subnets"

    # pylint: disable=arguments-differ
    def build( self, **_opts ):

        
        router1 = self.addNode( 'r0', cls=LinuxRouter, ip='10.0.0.1/24' )
        router2 = self.addNode( 'r1', cls=LinuxRouter, ip='10.0.1.1/24' )
        router3 = self.addNode( 'r2', cls=LinuxRouter, ip='10.0.2.1/24' )

        s1, s2, s3 = [ self.addSwitch( s ) for s in ( 's1', 's2', 's3' ) ]

        self.addLink( s1, router1, intfName2='r0-eth0',
                      params2={ 'ip' : '10.0.0.1/24'  } )  # for clarity
        self.addLink( s2, router2, intfName2='r1-eth0',
                      params2={ 'ip' : '10.0.1.1/24' } )
        self.addLink( s3, router3, intfName2='r2-eth0',
                      params2={ 'ip' :'10.0.2.1/24' } )
                      
                      
                      
                      
        
        self.addLink( router1, router2, intfName1="r0-eth1",intfName2='r1-eth1', params1={'ip':'10.0.3.1/24'},
                      params2={ 'ip' : '10.0.3.2/24'  } ) 
        self.addLink( router2, router3, intfName1="r1-eth2",intfName2='r2-eth1', params1={'ip':'10.0.4.1/24'},
                      params2={ 'ip' : '10.0.4.2/24'  } )
        self.addLink( router1, router3, intfName1="r0-eth2",intfName2='r2-eth2', params1={'ip':'10.0.5.1/24'},
                      params2={ 'ip' : '10.0.5.2/24'  } )  

        h1 = self.addHost('h1', ip='10.0.0.2/24', defaultRoute='via 10.0.0.1')
        h2 = self.addHost('h2', ip='10.0.0.3/24', defaultRoute='via 10.0.0.1')
        h3 = self.addHost('h3', ip='10.0.1.2/24', defaultRoute='via 10.0.1.1')
        h4 = self.addHost('h4', ip='10.0.1.3/24', defaultRoute='via 10.0.1.1')
        h5 = self.addHost('h5', ip='10.0.2.2/24', defaultRoute='via 10.0.2.1')
        h6 = self.addHost('h6', ip='10.0.2.3/24', defaultRoute='via 10.0.2.1')

        self.addLink(h1,s1)
        self.addLink(h2,s1)
        self.addLink(h3,s2)
        self.addLink(h4,s2)
        self.addLink(h5,s3)
        self.addLink(h6,s3)
       
       
def run():
    "Test linux router"
    topo = NetworkTopo()
    net = Mininet(topo = topo, controller = OVSController)
    info(net['r0'].cmd("ip route add 10.0.1.0/24 via 10.0.3.2"))
    info(net["r0"].cmd("ip route add 10.0.2.0/24 via 10.0.5.2"))
    info(net["r1"].cmd("ip route add 10.0.0.0/24 via 10.0.3.1"))
    info(net["r1"].cmd("ip route add 10.0.2.0/24 via 10.0.4.2"))
    info(net["r2"].cmd("ip route add 10.0.0.0/24 via 10.0.5.1"))
    info(net["r2"].cmd("ip route add 10.0.1.0/24 via 10.0.4.1"))
    net.start()
    CLI( net )
    net.stop()


if __name__ == '__main__':
    setLogLevel( 'info' )
    run()
