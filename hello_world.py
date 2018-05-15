import luigi
from time import sleep

class HelloTask(luigi.Task):
    def run(self):
        sleep(60)
        with open('tmp/hello.txt', 'w') as hello_file:
            hello_file.write('Hello')

    def output(self):
        return luigi.LocalTarget('tmp/hello.txt')

class WorldTask(luigi.Task):
    def run(self):
        sleep(30)
        with open('tmp/world.txt', 'w') as world_file:
            world_file.write('World')

    def output(self):
        return luigi.LocalTarget('tmp/world.txt')

class HelloWorldTask(luigi.Task):
    def run(self):
        sleep(60)
        with open('tmp/hello.txt') as hello_file:
            hello = hello_file.read()
        with open('tmp/world.txt') as world_file:
            world = world_file.read()
        with open('tmp/hello_world.txt', 'w') as output_file:
            content = '{} {}!'.format(hello, world)
            output_file.write(content)

    def output(self):
        return luigi.LocalTarget('tmp/hello_world.txt')

    def requires(self):
        return [HelloTask(), WorldTask()]

if __name__ == '__main__':
    luigi.run()
