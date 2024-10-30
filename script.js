function calcular() {
    const tipo = document.getElementById("tipo").value.toLowerCase();
    const ant = parseFloat(document.getElementById("ant").value);
    const nuv = parseFloat(document.getElementById("nuv").value);
    const pen = parseFloat(document.getElementById("pen").value);
    const pais = document.getElementById("pais").value.toLowerCase();

    let y;
    if (tipo === 'p') {
        y = "PARCIALMENTE USADA";
    } else if (tipo === 'n') {
        y = "NUEVA";
    } else {
        y = "INVÁLIDA";
    }

    const tarifas = {
        bolivia: 0.1497, colombia: 0.095, "costa rica": 0.05,
        salvador: 0.13, guatemala: 0.12, haiti: 0.1, honduras: 0.15,
        mexico: 0.16, nicaragua: 0.15, panama: 0.07, paraguay: 0.025,
        peru: 0.18, rd: 0.18, tt: 0.125, uruguay: 0.075, venezuela: 0.08,
        guyana: 0.15, surinam: 0.1, ecuador: 0.15
    };

    const por = tarifas[pais] || 0;
    const pag = nuv - ant;
    const porc = pag * por;
    const totdif = pag + porc;
    const penimp = (pen * por) + pen;
    const tottot = totdif + penimp;

    const resultados = `
        <p>La reserva es: <strong>${y}</strong></p>
        <p>DIFERENCIA = ${pag.toFixed(2)}, PORCENTUAL DEL ${(por * 100).toFixed(2)}% = ${porc.toFixed(2)}</p>
        <p>TOTAL DIFERENCIA = ${totdif.toFixed(2)}</p>
        <p>PENALIDAD = ${penimp.toFixed(2)}</p>
        <p>TOTAL A PAGAR = ${tottot.toFixed(2)}</p>
    `;

    document.getElementById("resultados").innerHTML = resultados;
}
