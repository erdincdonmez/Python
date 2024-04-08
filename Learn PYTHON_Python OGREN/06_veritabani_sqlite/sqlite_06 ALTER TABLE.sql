-- Yeni tabloyu oluştur
CREATE TABLE ogrenciler_temp (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    -- Diğer sütunlar buraya gelebilir
    adSoyad TEXT,
    numara INTEGER
);

-- Verileri yeni tabloya kopyala
INSERT INTO ogrenciler_temp (adSoyad, numara)
SELECT adSoyad, numara FROM ogrenciler;

-- Eski tabloyu sil
DROP TABLE ogrenciler;

-- Yeni tabloyu yeniden adlandır
ALTER TABLE ogrenciler_temp RENAME TO ogrenciler;
