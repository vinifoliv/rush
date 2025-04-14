from infra.cli.ifile_system import IFileSystem


class FileSystem(IFileSystem):
    def ler_arquivo(self, caminho: str) -> str:
        try:
            with open(caminho, "r") as arquivo:
                return arquivo.read()
        except FileNotFoundError as e:
            raise ValueError("Arquivo não encontrado.")
