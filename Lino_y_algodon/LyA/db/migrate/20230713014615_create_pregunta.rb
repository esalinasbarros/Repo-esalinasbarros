class CreatePregunta < ActiveRecord::Migration[7.0]
  def change
    create_table :pregunta do |t|
      t.references :producto, null: false, foreign_key: true
      t.text :texto

      t.timestamps
    end
  end
end
