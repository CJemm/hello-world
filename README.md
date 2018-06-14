<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>bbs club</title>
    <link rel="stylesheet" href="/static/css/bootstrap.min.css">
</head>
<body>
    <form class="form-horizontal" method="post" action="{{ url_for('.register') }}">
        <div class="control-group">
            <label class="control-label">用户名</label>
            <div class="controls">
                <input type="text" class="input-xlarge" name="username">
            </div>
        </div>
        <div class="control-group">
            <label class="control-label">密码</label>
            <div class="controls">
                <input type="text" class="input-xlarge" name="password">
            </div>
        </div>
        <div class="form-actions">
            <input type="submit" class="span-primary" value="注册">
        </div>
    </form>
    <form class="form-horizontal" method="post" action="{{ url_for('.login') }}">
        <div class="control-group">
            <label class="control-label">用户名</label>
            <div class="controls">
                <input type="text" class="input-xlarge" name="username">
            </div>
        </div>
        <div class="control-group">
            <label class="control-label">密码</label>
            <div class="controls">
                <input type="text" class="input-xlarge" name="password">
            </div>
        </div>
        <div class="form-actions">
            <input type="submit" class="span-primary" value="登录">
        </div>
    </form>
</body>
</html>
