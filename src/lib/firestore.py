from google.cloud import firestore

db = firestore.Client()

doc_ref = db.collection('any').document('test')

doc_ref.set({
    'campo': 'valor'
})


print(doc_ref.get('campo'))