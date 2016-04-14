from fabric.api import local


def basic():
    local('swagger-codegen generate -i specs/basic.json -l csharp -o ./tmp/')


def advanced():
    local('swagger-codegen generate -i specs/advanced.json -l csharp -o ./tmp/')


def internal():
    local('swagger-codegen generate -i specs/internal.json -l csharp -o ./tmp/')


def js():
    local('swagger-codegen generate -i specs/basic.json -l javascript -o ./tmp/')
