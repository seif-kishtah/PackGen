#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QVector>
#include <QString>

QT_BEGIN_NAMESPACE
namespace Ui {
class MainWindow;
}
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_Save_clicked();
    void on_Send_clicked();
    void on_clearLog_clicked();
    void on_DeleteSaved_clicked();
    void on_searchEdit_textChanged(const QString &text);


private:
    Ui::MainWindow *ui;
    QVector<QString> dataVector; // Vector to store input data

    void handleSendButtonClick(int row);

};
#endif // MAINWINDOW_H
