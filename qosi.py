import utils

def main():
    print('Getting data from server...')
    targets = utils.get_targets()
    if targets:
        print('OK')
    else:
        print('Error contacting the server!')
        return

    measurement = {}
    print('Getting information from device...')
    measurement['isp'] = utils.get_isp()
    print(measurement['isp'])
    measurement['os'] = utils.get_os()
    print(measurement['os'])
    #print(targets)
    
    for target, addr in targets.items():
        measurement['target'] = target
        print('Starting ICMP measurement to {}'.format(target))
        ping = utils.run_ping(addr)
        if ping:
            measurement['latency'] = ping['latency']
            print('Latency: {}ms'.format(measurement['latency']))
            measurement['jitter'] = ping['jitter']
            print('Jitter: {}ms'.format(measurement['jitter']))
            measurement['packet_loss'] = ping['packet_loss']
            print('Loss: {}%'.format(measurement['packet_loss']))
        else:
            print('Error, aborting')
            return

        print('Starting bandwidth measurement to {}'.format(target))
        iperf = utils.run_iperf(addr)
        if iperf:
            measurement['download'] = iperf['download']
            print('Download: {}Mbps'.format(measurement['download']))
            measurement['upload'] = iperf['upload']
            print('Upload: {}Mbps'.format(measurement['upload']))
        else:
            print('Error, aborting')
            return

        print('Sending results to databse...')
        if utils.send_results(measurement):
            print('OK')
        else:
            print('Error, aborting')
    print('Measurements finished.')


if __name__ == "__main__":
    main()
