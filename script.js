

function buttonClick() {
    let i1 = +document.getElementById("input1").value
    let i2 = +document.getElementById("input2").value

    let operator = document.querySelector('select[name="operatorSelect"]').value

    switch (operator) {
        case '+':
            result = i1 + i2
            break
        case '-':
            result = i1 - i2
            break
        case '*':
            result = i1 * i2
            break
        case '/':
            result = i1 / i2
            break
    }

    document.querySelector("body > div > p:nth-child(2)").innerHTML = "The result is: " + result
}