import sys


def write_stdout(s):
    """Write to stdout."""
    sys.stdout.write(s)
    sys.stdout.flush()


def write_stderr(s):
    """Write to stderr."""
    sys.stderr.write(s)
    sys.stderr.flush()


def main():
    """Main function."""
    while 1:
        write_stdout('READY\n')  # transition from ACKNOWLEDGED to READY
        line = sys.stdin.readline()  # read header line from stdin
        headers = dict([x.split(':') for x in line.split()])
        data = sys.stdin.read(int(headers['len']))  # read the event payload
        write_stdout('RESULT {}\n{}'.format(len(data), data))  # transition READY to ACKNOWLEDGED


def event_handler(event, response):
    """Event Handler."""
    line, data = response.split('\n', 1)
    headers = dict([x.split(':') for x in line.split()])
    lines = data.split('\n')
    prefix = '%s %s | '.format(headers['processname'], headers['channel'])
    print('\n'.join([prefix + l for l in lines]))

if __name__ == '__main__':
    main()
