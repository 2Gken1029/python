#!/usr/bin/env python3
# coding: utf-8

class Human():

    def __init__(self, name):
        # 名前
        self.name = name


class Patient(Human):
    def __init__(self, name, patient_id, symptom):
        super().__init__(name)

        # 症状
        self.symptom = symptom
        # 診察番号
        self.patient_id = patient_id

class Clinic():
    def __init__(self):
        # 患者リスト
        self.patients_list = []

    # 待ち人数表示
    def show_waiting_count(self):
        print(f'現在の待ち人数：{len(self.patients_list)}')

    # 予約
    def reserve(self, patient):
        if self._check_reserved(patient):
            print(f'{patient.name}さんは既に予約済みです．')
        else:
            print(f'{patient.name}さん予約完了')
            # 患者リストpatient_listにpatientを追加
            self.patients_list.append(patient)

    # 診察
    def diagnosis(self, patient_id=None):
        # 患者指定なしの場合順番に
        patient = None
        if patient_id == None:
            if len(self.patients_list)>0:
                patient = self.patients_list[0]
        else:
            for p in self.patients_list:
                if p.patient_id == patient_id:
                    patient = p

        # 診察患者がいない場合
        if patient == None:
            print('診察する患者がいません．')
        else:
            print(f'{patient.name}さん，{patient.symptom}ですね．')
            print(f'診察終わりました．お大事に．')

        # 患者リストpatients_listから除外
        self.patients_list.remove(patient)

    # 予約済み確認
    def _check_reserved(self, patient):
        for p in self.patients_list:
            # 引数のpatientとpatient_listの中のpatient_idの比較
            if p.patient_id == patient.patient_id:
                return True
        return False


def main():
    # Clinic Classのインスタンス
    myclinic = Clinic()

    print('---患者の数名の予約・待ち人数の表示を行う---')
    # 患者予約対象データ
    # name, age, symptomの順
    patients = [["佐藤", "111", "咳"],
                ["田中", "222", "腹痛"],
                ["鈴木", "333", "鼻水"],
                ["山田", "444", "倦怠感"],
                ["中田", "555", "インフルエンザ"],]

    # 患者予約
    for p in patients:
        name, age, symptom = p
        # loopで取得する name,age,symptomでPatientをインスタンス
        patient = Patient(name, age, symptom)
        # myclinicに予約 *reserveメソッド使用
        myclinic.reserve(patient)

    # 現在の待ち人数を表示
    myclinic.show_waiting_count()


    print('---重複した患者の予約---')
    # インスタンス
    me = Patient("中田", "555", "インフルエンザ")
    # 予約
    myclinic.reserve(me)
    # 現在の待ち人数を表示
    myclinic.show_waiting_count()


    print('---患者リスト順に表示して，待ち人数を表示する---')
    # 診察
    myclinic.diagnosis()
    # 現在の待ち人数を表示
    myclinic.show_waiting_count()


    print('---患者ID"555"を指定して，急患の診察を行う．待ち人数を表示する---')
    # 診察 patient_id 555指定
    myclinic.diagnosis(patient_id="555")
    # 現在の待ち人数を表示
    myclinic.show_waiting_count()

if __name__ == '__main__':
    main()