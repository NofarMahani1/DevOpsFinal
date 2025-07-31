function convert() {
  const unitType = document.getElementById("unit-type").value;
  const direction = parseInt(document.getElementById("direction").value);
  const input = parseFloat(document.getElementById("inputValue").value);
  const resultEl = document.getElementById("result");

  if (isNaN(input)) {
    resultEl.textContent = "Please enter a valid number.";
    return;
  }

  let result;

  switch (unitType) {
    case "temp":
      result =
        direction === 1
          ? (input * 9) / 5 + 32 // C → F
          : ((input - 32) * 5) / 9; // F → C
      resultEl.textContent = `Result: ${result.toFixed(2)}°`;
      break;

    case "length":
      result =
        direction === 1
          ? input * 3.28084 // M → ft
          : input / 3.28084; // ft → M
      resultEl.textContent = `Result: ${result.toFixed(2)} ${
        direction === 1 ? "ft" : "m"
      }`;
      break;

    case "weight":
      result =
        direction === 1
          ? input * 2.20462 // kg → lb
          : input / 2.20462; // lb → kg
      resultEl.textContent = `Result: ${result.toFixed(2)} ${
        direction === 1 ? "lb" : "kg"
      }`;
      break;
  }
}
