def test_nginx(host):
    nginx_version = host.run("nginx -v")
    assert nginx_version.stderr=="nginx version: nginx/1.14.0 (Ubuntu)\n"
    assert host.file("/etc/nginx/conf.d/server.conf").exists
    assert host.file("/usr/share/nginx/html/index.html").exists