import pytest

def test_mcj_install_dir(host):

    mcj_install_dir = host.file('/opt/minecraft')
    assert mcj_install_dir.exists
    assert mcj_install_dir.is_directory
    assert mcj_install_dir.mode == 0o755

def test_install_bin_dir(host):

    install_bin_dir = host.file('/opt/minecraft/bin')
    assert install_bin_dir.exists
    assert install_bin_dir.is_directory
    assert install_bin_dir.mode == 0o755

def test_install_workspace_dir(host):

    install_workspace_dir = host.file('/opt/minecraft/workspace')
    assert install_workspace_dir.exists
    assert install_workspace_dir.is_directory
    assert install_workspace_dir.mode == 0o755

def test_server_jar_file(host):

    server_jar_file = host.file('/opt/minecraft/bin/minecraft_server.1.21.jar')
    assert server_jar_file.exists
    assert server_jar_file.is_file
    assert server_jar_file.mode == 0o644

def test_server_jar_symlink(host):

    server_jar_symlink = host.file('/opt/minecraft/bin/minecraft_server.jar')
    assert server_jar_symlink.exists
    assert server_jar_symlink.is_symlink

def test_server_start_script(host):

    server_start_script = host.file('/opt/minecraft/bin/start.sh')
    assert server_start_script.exists
    assert server_start_script.is_file
    assert server_start_script.mode == 0o755
    assert server_start_script.contains('java -Xmx2048M -Xms1024M -jar /opt/minecraft/bin/minecraft_server.jar nogui')
