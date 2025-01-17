/*
 * MainWindow Class Implementation
 * 
 * This class represents the main window of the application. It provides a user interface
 * for sending and saving data, as well as managing the displayed data in tables.
 * 
 * Member Functions:
 * 
 * - MainWindow(QWidget *parent)
 *   Constructor that initializes the main window and sets up the user interface.
 *   Connects signals and slots for the search functionality and clear log button.
 * 
 * - ~MainWindow()
 *   Destructor that cleans up the UI components.
 * 
 * - void on_Send_clicked()
 *   Handles the click event of the "Send" button. Validates input fields, collects data
 *   from the input fields, and appends the data to the "SendTable". Clears the input fields
 *   after sending.
 * 
 * - void on_Save_clicked()
 *   Handles the click event of the "Save" button. Validates input fields, collects data
 *   from the input fields, and appends the data to the "SaveTable". Adds a "Send" button
 *   to each row in the "SaveTable" for later use. Clears the input fields after saving.
 * 
 * - void on_DeleteSaved_clicked()
 *   Handles the click event of the "Delete" button. Removes the selected row from the
 *   "SaveTable" if a row is selected.
 * 
 * - void on_searchEdit_textChanged(const QString &text)
 *   Filters the rows in the "SaveTable" based on the search term entered in the search
 *   field. Rows that do not match the search term are hidden.
 * 
 * - void handleSendButtonClick(int row)
 *   Handles the click event of the "Send" button in the "SaveTable". Extracts data from
 *   the selected row and appends it to the "SendTable".
 * 
 * - void on_clearLog_clicked()
 *   Clears all rows in the "SendTable" when the "Clear Log" button is clicked.
 */


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
    dataVector.clear();

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
    dataVector.append(Name);
    dataVector.append(Address);
    dataVector.append(Port);
    dataVector.append(Type);
    dataVector.append(ASCII);
    dataVector.append(Hex);

    int row = ui->SendTable->rowCount();
    ui->SendTable->insertRow(row);
    QString Time = QDateTime::currentDateTime().toString("yyyy-MM-dd hh:mm:ss");
    ui->SendTable->setItem(row, 0, new QTableWidgetItem(Time));

    for (int col = 0; col < dataVector.size(); ++col) {

        QTableWidgetItem *item = new QTableWidgetItem(dataVector[col]);
        ui->SendTable->setItem(row, col+1, item);

    }

    ui->Name->clear();
    ui->ASCII->clear();
    ui->Address->clear();
    ui->Port->clear();
}
void MainWindow::on_Save_clicked()
{
    dataVector.clear();

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
    dataVector.append(Name);
    dataVector.append(Address);
    dataVector.append(Port);
    dataVector.append(Type);
    dataVector.append(ASCII);
    dataVector.append(Hex);


    int row = ui->SaveTable->rowCount();
    ui->SaveTable->insertRow(row);

    QPushButton *sendButton = new QPushButton("Send");
    ui->SaveTable->setCellWidget(row, 0, sendButton);

    connect(sendButton, &QPushButton::clicked, this, [this, row]() {
        handleSendButtonClick(row); // Pass the row number to the slot
    });

    for (int col = 0; col < dataVector.size(); ++col) {

            QTableWidgetItem *item = new QTableWidgetItem(dataVector[col]);
            ui->SaveTable->setItem(row, col+1, item);

    }

   
    ui->Name->clear();
    ui->ASCII->clear();
    ui->Address->clear();
    ui->Port->clear();
}
void MainWindow::on_DeleteSaved_clicked()
{
    int selectedRow = ui->SaveTable->currentRow();

    if (selectedRow >= 0) {
        // Remove the selected row
        ui->SaveTable->removeRow(selectedRow);
    } else {
        QMessageBox::warning(this, "No Selection", "Please select a row to delete.");
    }
}
void MainWindow::on_searchEdit_textChanged(const QString &text)
{
    QString searchTerm = text.trimmed();

    for (int row = 0; row < ui->SaveTable->rowCount(); ++row) {
        bool matchFound = searchTerm.isEmpty(); // Show all rows if the search term is empty

        for (int col = 0; col < ui->SaveTable->columnCount(); ++col) {
            QTableWidgetItem *item = ui->SaveTable->item(row, col);

            if (item && item->text().contains(searchTerm, Qt::CaseInsensitive)) {
                matchFound = true;
                break; // No need to check other columns in this row
            }
        }

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

    QString Time = QDateTime::currentDateTime().toString("yyyy-MM-dd hh:mm:ss");

    int newRow = ui->SendTable->rowCount();
    ui->SendTable->insertRow(newRow);

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
