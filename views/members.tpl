<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Members</title>

    <style>
        body {
            background-color: lemonchiffon
        }
    </style>
</head>
<body>
    <h2>Members:</h2>
    <table>
        % for row in rows:
            <tr>
                % for col in row:
                    <td>{{col}}</td>
                % end
            </tr>
        % end
    </table>
    <a href="/">Aftur á heimasíðu</a>
</body>
</html>