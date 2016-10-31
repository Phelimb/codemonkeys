import hug

API = hug.API('git')


@hug.object(name='git', version='1.0.0', api=API)
@hug.object.urls('/', requires=())
class GIT(object):

    """An example of command like calls via an Object"""

    @hug.object.cli
    @hug.object.get('/push')
    def push(self, k, branch='master'):
        return 'Pushing {}'.format(branch)

    @hug.object.cli
    @hug.object.get('/pull')
    def pull(self, k, branch='master'):
        return 'Pulling {}'.format(branch)


if __name__ == '__main__':
    API.cli()
