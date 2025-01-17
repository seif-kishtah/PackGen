#include "mainwindow.h"
#include "./ui_mainwindow.h"
#include <QMessageBox>
#include <QDateTime>


MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    connect(ui->searchEdit, &QLineEdit::textChanged, this, &MainWindow::on_searchEdit_textChanged);
    connect(ui->clearLog, &QPushButton::clicked, this, &MainWindow::on_clearLog_clicked);
}

MainWindow::~MainWindow()
{
    delete ui;
}
void MainWindow::on_Send_clicked()
{
    // Clear the vector before storing new data
    dataVector.clear();

    // Get text from QLineEdit widgets
    QString Name = ui->NameEdit->text();
    QString ASCII = ui->ASCIIEdit->text();
    QString Hex = ui->HEXEdit->text();
    QString Address=ui->AddressEdit->text();
    QString Port=ui->PortEdit->text();
    QString Type = ui->Type->currentText();

    if (Name.isEmpty() || ASCII.isEmpty() || Hex.isEmpty() || Address.isEmpty() || Port.isEmpty()) {
        QMessageBox::warning(this, "Empty Fields", "All fields must be filled out.");
        return; // Exit the function if any field is empty
    }
    // Store the inputs in the vector
    dataVector.append(Name);
    dataVector.append(Address);
    dataVector.append(Port);
    dataVector.append(Type);
    dataVector.append(ASCII);
    dataVector.append(Hex);




    // Add a new row to the table
    int row = ui->SendTable->rowCount();
    ui->SendTable->insertRow(row);
    QString Time = QDateTime::currentDateTime().toString("yyyy-MM-dd hh:mm:ss");
    ui->SendTable->setItem(row, 0, new QTableWidgetItem(Time));



    // Populate the table with the vector data
    for (int col = 0; col < dataVector.size(); ++col) {

        QTableWidgetItem *item = new QTableWidgetItem(dataVector[col]);
        ui->SendTable->setItem(row, col+1, item);

    }

    // Clear the QLineEdit widgets after adding the data
    ui->Name->clear();
    ui->ASCII->clear();
    ui->Address->clear();
    ui->Port->clear();
}
void MainWindow::on_Save_clicked()
{
    // Clear the vector before storing new data
    dataVector.clear();

    // Get text from QLineEdit widgets
    QString Name = ui->NameEdit->text();
    QString ASCII = ui->ASCIIEdit->text();
    QString Hex = ui->HEXEdit->text();
    QString Address=ui->AddressEdit->text();
    QString Port=ui->PortEdit->text();
    QString Type = ui->Type->currentText();

    if (Name.isEmpty() || ASCII.isEmpty() || Hex.isEmpty() || Address.isEmpty() || Port.isEmpty()) {
        QMessageBox::warning(this, "Empty Fields", "All fields must be filled out.");
        return; // Exit the function if any field is empty
    }
    // Store the inputs in the vector
    dataVector.append(Name);
    dataVector.append(Address);
    dataVector.append(Port);
    dataVector.append(Type);
    dataVector.append(ASCII);
    dataVector.append(Hex);




    // Add a new row to the table
    int row = ui->SaveTable->rowCount();
    ui->SaveTable->insertRow(row);

    QPushButton *sendButton = new QPushButton("Send");
    ui->SaveTable->setCellWidget(row, 0, sendButton);

    // Connect the "Send" button to a slot
    connect(sendButton, &QPushButton::clicked, this, [this, row]() {
        handleSendButtonClick(row); // Pass the row number to the slot
    });

    // Populate the table with the vector data
    for (int col = 0; col < dataVector.size(); ++col) {

            QTableWidgetItem *item = new QTableWidgetItem(dataVector[col]);
            ui->SaveTable->setItem(row, col+1, item);

    }

    // Clear the QLineEdit widgets after adding the data
    ui->Name->clear();
    ui->ASCII->clear();
    ui->Address->clear();
    ui->Port->clear();
}
void MainWindow::on_DeleteSaved_clicked()
{
    // Get the currently selected row
    int selectedRow = ui->SaveTable->currentRow();

    // Check if a row is selected
    if (selectedRow >= 0) {
        // Remove the selected row
        ui->SaveTable->removeRow(selectedRow);
    } else {
        // Show a message if no row is selected
        QMessageBox::warning(this, "No Selection", "Please select a row to delete.");
    }
}
void MainWindow::on_searchEdit_textChanged(const QString &text)
{
    // Get the search term from the QLineEdit
    QString searchTerm = text.trimmed();

    // Iterate through all rows in the table
    for (int row = 0; row < ui->SaveTable->rowCount(); ++row) {
        bool matchFound = searchTerm.isEmpty(); // Show all rows if the search term is empty

        // Iterate through all columns in the row
        for (int col = 0; col < ui->SaveTable->columnCount(); ++col) {
            QTableWidgetItem *item = ui->SaveTable->item(row, col);

            // Check if the item exists and contains the search term
            if (item && item->text().contains(searchTerm, Qt::CaseInsensitive)) {
                matchFound = true;
                break; // No need to check other columns in this row
            }
        }

        // Show or hide the row based on whether a match was found
        ui->SaveTable->setRowHidden(row, !matchFound);
    }
}
void MainWindow::handleSendButtonClick(int row)
{
    // Extract data from the selected row in SaveTable
    QString Address = ui->SaveTable->item(row, 2)->text(); // Column 2: Address
    QString Port = ui->SaveTable->item(row, 3)->text();    // Column 3: Port
    QString Method = ui->SaveTable->item(row, 4)->text();  // Column 4: Method (Type)
    QString ASCII = ui->SaveTable->item(row, 5)->text();   // Column 5: ASCII
    QString Hex = ui->SaveTable->item(row, 6)->text();     // Column 6: Hex

    // Get the current time
    QString Time = QDateTime::currentDateTime().toString("yyyy-MM-dd hh:mm:ss");

    // Add a new row to the SendTable
    int newRow = ui->SendTable->rowCount();
    ui->SendTable->insertRow(newRow);

    // Populate the SendTable with the extracted data
    ui->SendTable->setItem(newRow, 0, new QTableWidgetItem(Time));
    ui->SendTable->setItem(newRow, 1, new QTableWidgetItem(Address));
    ui->SendTable->setItem(newRow, 2, new QTableWidgetItem(Port));
    ui->SendTable->setItem(newRow, 3, new QTableWidgetItem(Method));
    ui->SendTable->setItem(newRow, 4, new QTableWidgetItem(ASCII));
    ui->SendTable->setItem(newRow, 5, new QTableWidgetItem(Hex));
}
void MainWindow::on_clearLog_clicked()
{
    // Clear all rows in the SendTable
    ui->SendTable->setRowCount(0);
}
