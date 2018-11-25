var planilha = SpreadsheetApp.openById("14MHJf_QGHokwXvWjk3Dqm2jMBinB6odz-g1L3jynlJI"); 
var sheet = planilha.getActiveSheet();

function doGet(e)

{
  var txt1 = "Temperatura:";
  var txt2 = "Horario:";
  var txt3 = "Humidade:";
  var txt4 = "Data:";
  var linhas = sheet.getLastRow();
  var rec_horario = e.parameter.horario;
  var rec_temperatura = e.parameter.temperatura;
  var rec_humidade = e.parameter.humidade;
  var rec_dataatual = e.parameter.dataatual;
  sheet.appendRow([txt1,rec_temperatura,txt2,rec_horario,txt3,rec_humidade,txt4,rec_dataatual]);   
  return ContentService.createTextOutput("Temperatura recebida!");
}