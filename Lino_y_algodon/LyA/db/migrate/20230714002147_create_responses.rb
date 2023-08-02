class CreateResponses < ActiveRecord::Migration[7.0]
  def change
    create_table :responses do |t|
      t.string :texto
      t.references :pregunta, null: false, foreign_key: true

      t.timestamps
    end
  end
end
