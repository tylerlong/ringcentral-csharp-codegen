from fabric.api import local


def generate(spec = 'advanced', language = 'csharp'):
    local('swagger-codegen generate -i specs/{0}.json -l {1} -o ./tmp/'.format(spec, language))
